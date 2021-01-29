from DialogFrameSimple import DialogFrameSimple
from DialogAct import DialogAct
from DialogActTypes import DialogActTypes

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
        if newSemanticFrame.Intent == "INFORM":
            for slot in newSemanticFrame.Slots:
                self.DialogFrame.slots[slot] = newSemanticFrame.Slots[slot]
        #elif newSemanticFrame.Intent == "REORDER":
        #    self.DialogFrame.reorder = True
        elif newSemanticFrame.Intent == "CONFIRM":
            self.DialogFrame.slots["confirmed"] = True
            #for slot in self.DialogFrame.check_info:
            #    self.DialogFrame[slot] = self.DialogFrame.check_info[slot]
        elif newSemanticFrame.Intent == "DENY":
            self.DialogFrame.slots["confirmed"] = False
            #for slot in self.DialogFrame.prev_Dialog_Act:
            #    self.DialogFrame[slot] = ""

        return

    def selectDialogAct(self):
        # decide on what dialog act to execute
        dialogAct = DialogAct()

        for slot in self.DialogFrame.slots:
            if self.DialogFrame.slots[slot] == "":
                if slot == "order_address":
                    if self.DialogFrame.slots["order_delivery"] == "":
                        dialogAct.DialogActType = DialogActTypes.REQUEST
                        dialogAct.info_type = "order_delivery"
                    elif self.DialogFrame.slots["order_delivery"] == "pick-up":
                        self.DialogFrame.slots[slot] = None
                    else:
                        dialogAct.DialogActType = DialogActTypes.REQUEST
                        dialogAct.info_type = slot
                        return dialogAct
                else:
                    dialogAct.DialogActType = DialogActTypes.REQUEST
                    dialogAct.info_type = slot
                    return dialogAct

        if self.DialogFrame.slots["confirmed"]:
            dialogAct.DialogActType = DialogActTypes.GOODBYE
        else:
            dialogAct.DialogActType = DialogActTypes.REQUEST
            dialogAct.info_type = "confirmed"
            dialogAct.content = self.DialogFrame

        # by default, return a Hello dialog act
        if dialogAct.DialogActType == DialogActTypes.UNDEFINED:
            dialogAct.DialogActType = DialogActTypes.HELLO

        return dialogAct
