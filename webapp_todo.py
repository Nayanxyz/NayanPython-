import streamlit as st

import FunctionComb as fc

todos = fc.todos_f()

def add_todo():
    todoo = st.session_state["new_todo"] + '\n'             #session state is a type of dictionary
                                                              # like values in gui that calls key and their values
    todos.append(todoo)
    fc.todos_w(todos)

st.title("MY TODO APP")
st.subheader("add whatever you like")                          #to write sub header
st.write("LOL")                                               #write method to write simple lines

for todo in todos:
    st.checkbox(todo)                                         #chechbox method for creating checkboxes

st.text_input(label="umm...", placeholder="Add new todo...", on_change=add_todo, key="new_todo")

#[ st.session_state ] this helps us see whats going on in the code