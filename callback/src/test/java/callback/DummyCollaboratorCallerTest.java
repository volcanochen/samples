package callback;

import static org.hamcrest.CoreMatchers.any;
import static org.hamcrest.CoreMatchers.anything;
import static org.hamcrest.CoreMatchers.equalTo;
import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertThat;
import static org.mockito.Mockito.doAnswer;
import static org.mockito.Mockito.times;
import static org.mockito.Mockito.verify;

import java.util.Arrays;
import java.util.List;

import org.junit.Before;
import org.junit.Test;
import org.mockito.ArgumentCaptor;
import org.mockito.Captor;
import org.mockito.Mock;
import org.mockito.Mockito;
import org.mockito.MockitoAnnotations;
import org.mockito.invocation.InvocationOnMock;
import org.mockito.stubbing.Answer;

public class DummyCollaboratorCallerTest {

    // Ҫ���Ե�����
    private DummyCaller dummyCaller;

    @Mock
    private DummyCollaborator mockDummyCollaborator;

    @Captor
    private ArgumentCaptor<DummyCallback> dummyCallbackArgumentCaptor;

    @Before
    public void setUp() {
        MockitoAnnotations.initMocks(this);
        dummyCaller = new DummyCaller(mockDummyCollaborator);
    }
    
    @Test
    public void testDoSomethingAsynchronouslyUsingDoAnswer() {
        
        final List<String> results = Arrays.asList("One", "Two", "Three");
        // Ϊcallbackִ��һ��ͬ��anwser
        doAnswer(new Answer() {
            @Override
            public Object answer(InvocationOnMock invocation) throws Throwable {
                ((DummyCallback) invocation.getArguments()[0]).onSuccess(results);
                return null;
            }
        }).when(mockDummyCollaborator).doSomethingAsynchronously(Mockito.any());

        // ���ñ����Եĺ���
        dummyCaller.doSomethingAsynchronously();

        // ��֤״̬����
        verify(mockDummyCollaborator, times(1)).doSomethingAsynchronously(Mockito.any());
        assertThat(dummyCaller.getResult(), is(equalTo(results)));
    }
    @Test
    public void testDoSomethingAsynchronouslyUsingArgumentCaptor() {
        // ����Ҫ�����Է�����
        dummyCaller.doSomethingAsynchronously();

        final List<String> results = Arrays.asList("One", "Two", "Three");

        // Let's call the callback. ArgumentCaptor.capture() works like a matcher.
        verify(mockDummyCollaborator, times(1)).doSomethingAsynchronously(
                dummyCallbackArgumentCaptor.capture());

        // ��ִ�лص�֮ǰ��֤���
        assertThat(dummyCaller.getResult().isEmpty(), is(true));

        // ���ûص���onSuccess����
        dummyCallbackArgumentCaptor.getValue().onSuccess(results);

        // �ٴ���֤���
        assertThat(dummyCaller.getResult(), is(equalTo(results)));
    }
}