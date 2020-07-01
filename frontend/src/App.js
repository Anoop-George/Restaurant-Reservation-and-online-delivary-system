import React from "react";
import { render } from "react-dom";
import Base from "./components/base";
import rootReducer from "./reducers/rootReducer";
import { createStore } from "redux";
import { Provider } from "react-redux";
import thunk from "redux-thunk";

const store = createStore(rootReducer, applyMiddleware(thunk));

function App() {
  return (
    <div>
      <Provider store={store}>
        <Base />
      </Provider>
    </div>
  );
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
