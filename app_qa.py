import time
from rag import RagService
import streamlit as st
import config_data as config

# 标题
st.title("智能客服")
st.divider()

# 保证记录不丢！
if "message" not in st.session_state:
    st.session_state["message"] = [{"role": "assistant", "content" : "有什么可帮助你？"}]

if "rag" not in st.session_state:
    st.session_state["rag"] = RagService()

for message in st.session_state["message"]:
    st.chat_message(message["role"]).write(message["content"])

# 在页面最下面提供用户输入栏
prompt = st.chat_input()

if prompt:

    # 在页面输出用户的提问
    st.chat_message("user").write(prompt)
    st.session_state["message"].append({"role" : "user", "content": prompt})

    ai_res_list = []
    with st.spinner("ai思考中"):
        res_stream = st.session_state["rag"].chain.stream({"input": prompt},config.session_config)

        def capture(generator,cache_list):
            for chunk in generator:   # 遍历流式输出的每一小块文字
                cache_list.append(chunk)   # 👈 偷偷存起来！
                yield chunk  # 👈 继续往外吐，给前端显示打字机效果

        st.chat_message("assistant").write_stream(capture(res_stream,ai_res_list))
        st.session_state["message"].append({"role" : "assistant", "content": "".join(ai_res_list)})

        # ["a","b","c"] "".join(list)  -> abc
        # ["a","b","c"] ",".join(list)  -> a,b,c


