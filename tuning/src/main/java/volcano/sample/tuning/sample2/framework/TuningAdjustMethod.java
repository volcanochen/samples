package volcano.sample.tuning.sample2.framework;

public class TuningAdjustMethod {

    public enum OPCODE {
        DONE, ADJUST
    };

    OPCODE operationCode;

    public enum OPVALUE {
        STEP_FORWARD, 
        STEP_BACK, 
        STEP_RANDON, 
        MIN,
        MAX
    };

    OPVALUE operationValue;

    public TuningAdjustMethod(OPCODE i, OPVALUE j) {
        operationCode = i;
        operationValue = j;
    }

    public boolean isEnd() {

        if (operationCode == OPCODE.DONE) {
            return true;
        }

        return false;

    }

    public OPVALUE getOperationValue() {
        return operationValue;
    }

}
