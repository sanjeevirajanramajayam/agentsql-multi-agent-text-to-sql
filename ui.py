import streamlit as st
import requests

st.set_page_config(page_title="AgentSQL", page_icon="🤖", layout="wide")

st.title("AgentSQL: Natural Language to SQL")
st.markdown("Ask questions about the Chinook database in plain English!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "sql_query" in message:
            with st.expander("Generated SQL Query"):
                st.code(message["sql_query"], language="sql")
        if "result" in message:
            with st.expander("Database Result"):
                st.write(message["result"])

# React to user input
if prompt := st.chat_input("What are the top 5 best-selling tracks?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Call FastAPI backend
    with st.chat_message("assistant"):
        with st.spinner("AgentSQL is thinking..."):
            try:
                response = requests.post(
                    "http://localhost:8000/query",
                    json={"question": prompt},
                    timeout=60
                )
                if response.status_code == 200:
                    data = response.json()
                    answer = data.get("answer", "I couldn't generate an answer.")
                    sql_query = data.get("sql_query", "")
                    db_result = data.get("result", "")
                    
                    st.markdown(answer)
                    
                    if sql_query:
                        with st.expander("Generated SQL Query"):
                            st.code(sql_query, language="sql")
                            
                    if db_result:
                        with st.expander("Database Result"):
                            st.write(db_result)
                            
                    # Add assistant response to chat history
                    st.session_state.messages.append({
                        "role": "assistant", 
                        "content": answer,
                        "sql_query": sql_query,
                        "result": db_result
                    })
                else:
                    st.error(f"Error from server: {response.status_code}")
                    st.write(response.text)
            except requests.exceptions.RequestException as e:
                st.error(f"Failed to connect to backend. Is it running? Error: {e}")
