import streamlit as st
import functions

"""
🧠 Qu'est-ce que st.session_state ?
st.session_state est un dictionnaire spécial dans Streamlit qui conserve 
les valeurs des widgets (comme text_input, checkbox, slider, etc.) 
entre les interactions (par exemple quand tu appuies sur "Entrée", 
changes une case, etc.).
Il est super utile pour :
    Récupérer ou mémoriser des valeurs de champs
    Suivre l’état d’un champ ou widget sur plusieurs interactions
    Agir quand un champ est modifié
"""


def add_todo():
    todo = st.session_state["NEW_TODO"] +"\n"
    todos.append(todo)
    functions.write_todos(todos)
    print(todo)


todos =  functions.get_todos()
# to run the page use the terminal: streamlit run webGUI.py
st.title("My Todo App")
st.subheader("This is my Todo app. ")
st.write("Thos app is to increase your productivity.")  
# lines should not be more than 75 characters long, in a half window set up

for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"todo_{i}")  # ✔️ chaque case a une clé "unique", we can use key=todo, without using enumerate
    if checkbox:
        todos.pop(i)
        functions.write_todos(todos)
        del st.session_state[f"todo_{i}"]   # delet the pain from the session state
        # st.experimental_rerun()

"""
for todo in todos:
    st.checkbox(todo)  # ❌ Streamlit plante ici à cause du label dupliqué
Cela signifie que tu as plusieurs st.checkbox() avec exactement le même texte (label), ce qui fait que Streamlit 
génère plusieurs fois le même identifiant interne → ce qu'il n’autorise pas.
    """

#st.text_input("")   # equivalent to st.text_input(label="")
st.text_input("Enter a Todo", placeholder="Add new todo...",
              on_change=add_todo, key="NEW_TODO")

#print("Hello")        # proves that everytime we reload our web page, the script is executed

st.session_state   # to see the dictionary in the end


import streamlit as st
print(st.__version__)
print(hasattr(st, "experimental_rerun"))  # Doit maintenant être True