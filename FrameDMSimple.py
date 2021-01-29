from DialogFrameSimple import DialogFrameSimple
from DialogAct import DialogAct
from DialogActTypes import DialogActTypes
from Database import Database

class FrameDMSimple:

    def __init__(self, NLU, NLG):
        self.NLU = NLU
        self.NLG = NLG
        # define frame below, for example:
        self.DialogFrame = DialogFrameSimple()

    def execute(self, inputStr):
        # apply the NLU component
        currentSemanticFrame = self.NLU.parse(inputStr)

        # update the dialog frame with the new information
        self.trackState(currentSemanticFrame)

        # and decide what to do next
        newDialogAct = self.selectDialogAct()

        # then generate some meaningful response
        response = self.NLG.generate(newDialogAct) 
        return response

    def trackState(self, newSemanticFrame):
        # update self.DialogFrame based on the contents of newSemanticFrame

        # Catch reorder request in order to change DialogFrame to database version
        if self.DialogFrame.reorder and "order_phone" in newSemanticFrame.Slots:
            existing_info = DialogFrameSimple()
            print(newSemanticFrame.Slots)
            existing_info.build_from_database(Database.customers[newSemanticFrame.Slots["order_phone"]])
            self.DialogFrame = existing_info
            return

        # Fill in given info, or update DialogFrame with user-initiated requests
        if newSemanticFrame.Intent == "INFORM":
            for slot in newSemanticFrame.Slots:
                self.DialogFrame.slots[slot] = newSemanticFrame.Slots[slot]
        elif newSemanticFrame.Intent == "REORDER":
            self.DialogFrame.reorder = True
        elif newSemanticFrame.Intent == "START-OVER":
            self.DialogFrame = DialogFrameSimple()
            self.DialogFrame.restart = True
        elif newSemanticFrame.Intent == "CANCEL":
            self.DialogFrame = DialogFrameSimple()
            self.DialogFrame.give_up = True
        elif newSemanticFrame.Intent == "REPEAT":
            self.DialogFrame.repeat = True
        elif newSemanticFrame.Intent == "CHECK_ORDER":
            self.DialogFrame.time = True
        elif newSemanticFrame.Intent == "CONFIRM":
            self.DialogFrame.slots["confirmed"] = True
            #for slot in self.DialogFrame.check_info:
            #    self.DialogFrame[slot] = self.DialogFrame.check_info[slot]
        elif newSemanticFrame.Intent == "DENY":
            self.DialogFrame.slots["confirmed"] = False
            self.DialogFrame.wrong_info = True
            #for slot in self.DialogFrame.prev_Dialog_Act:
            #    self.DialogFrame[slot] = ""

        return

    def selectDialogAct(self):
        # decide on what dialog act to execute
        dialogAct = DialogAct()

        # Get phone number for lookup if reordering
        if self.DialogFrame.reorder:
            dialogAct.DialogActType = DialogActTypes.REQUEST
            dialogAct.info_type = "order_phone"

            self.DialogFrame.prev_Dialog_Act = dialogAct
            return dialogAct

        # Start over, Cancel, Repeat, Check order
        if self.DialogFrame.restart:
            dialogAct.DialogActType = DialogActTypes.HELLO
            self.DialogFrame.restart = False

            self.DialogFrame.prev_Dialog_Act = dialogAct
            return dialogAct
        elif self.DialogFrame.give_up:
            dialogAct.DialogActType = DialogActTypes.GOODBYE

            self.DialogFrame.prev_Dialog_Act = dialogAct
            return dialogAct
        elif self.DialogFrame.repeat:
            dialogAct = self.DialogFrame.prev_Dialog_Act
            self.DialogFrame.repeat = False

            self.DialogFrame.prev_Dialog_Act = dialogAct
            return dialogAct
        elif self.DialogFrame.time:
            dialogAct.DialogActType = DialogActTypes.INFORM
            dialogAct.info_type = "wait_time"
            dialogAct.content = self.DialogFrame
            self.DialogFrame.time = False

            self.DialogFrame.prev_Dialog_Act = dialogAct
            return dialogAct


        # Request missing information
        for slot in self.DialogFrame.slots:
            if self.DialogFrame.slots[slot] == "":
                if slot == "order_address":
                    if self.DialogFrame.slots["order_delivery"] == "":
                        dialogAct.DialogActType = DialogActTypes.REQUEST
                        dialogAct.info_type = "order_delivery"

                        self.DialogFrame.prev_Dialog_Act = dialogAct
                        return dialogAct
                    elif self.DialogFrame.slots["order_delivery"] == "pick-up":
                        self.DialogFrame.slots[slot] = None
                    else:
                        dialogAct.DialogActType = DialogActTypes.REQUEST
                        dialogAct.info_type = slot

                        self.DialogFrame.prev_Dialog_Act = dialogAct
                        return dialogAct
                else:
                    dialogAct.DialogActType = DialogActTypes.REQUEST
                    dialogAct.info_type = slot

                    self.DialogFrame.prev_Dialog_Act = dialogAct
                    return dialogAct

        # Confirm or correct order information
        if self.DialogFrame.slots["confirmed"]:
            dialogAct.DialogActType = DialogActTypes.GOODBYE
            dialogAct.info_type = "successful"

            self.DialogFrame.prev_Dialog_Act = dialogAct
            return dialogAct
        elif self.DialogFrame.wrong_info:
            dialogAct.DialogActType = DialogActTypes.REQUEST
            dialogAct.info_type = "correction"
            self.DialogFrame.wrong_info = False

            self.DialogFrame.prev_Dialog_Act = dialogAct
            return dialogAct
        else:
            dialogAct.DialogActType = DialogActTypes.REQUEST
            dialogAct.info_type = "confirmed"
            dialogAct.content = self.DialogFrame

            self.DialogFrame.prev_Dialog_Act = dialogAct
            return dialogAct

