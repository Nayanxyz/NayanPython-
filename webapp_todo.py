import streamlit as st

import FunctionComb as fc

todos = fc.todos_f()

def add_todo():
    todoo = st.session_state["new_todo"] + '\n'             #session state is a type of dictionary
    todos.append(todoo)                                                        # like values in gui that calls key and their values
    fc.todos_w(todos)
    st.session_state["new_todo"] = ""                        #when we again command st.session_state , streamlit reruns new_todo key and
                                                             # gives the vale that is  "" empty .SO it refreshes input box


st.title("MY TODO APP")                                         #if we place st.title below write , it will be shown below write on the web page
st.subheader("add whatever you like")                          #to write sub header
st.write("LOL")                                               #write method to write simple lines

for variable, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)                                         #checkbox method for creating checkboxes
    if checkbox:
        todos.pop(variable)
        fc.todos_w(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="umm...", placeholder="Add new todo...", on_change=add_todo, key="new_todo")

#[ st.session_state ] this helps us see whats going on in the code