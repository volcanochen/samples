package callback;

import java.util.ArrayList;
import java.util.List;

public class DummyCaller implements DummyCallback {
    // 执行异步操作的代理类
    private final DummyCollaborator dummyCollaborator;
    // 执行结果
    private List<String> result = new ArrayList<String>();

    public DummyCaller(DummyCollaborator dummyCollaborator) {
        this.dummyCollaborator = dummyCollaborator;
    }

    public void doSomethingAsynchronously() {
        dummyCollaborator.doSomethingAsynchronously(this);
    }

    public List<String> getResult() {
        return this.result;
    }

    @Override
    public void onSuccess(List<String> result) {
        this.result = result;
        System.out.println("On success");
    }

    @Override
    public void onFail(int code) {
        System.out.println("On Fail");
    }
}