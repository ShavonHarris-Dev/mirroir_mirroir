import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './Components/Login';
import FriendList from './Components/FriendList';
import MessageBox from './Components/MessageBox';
import SendMessage from './Components/SendMessage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route
          path="/"
          element={
            <div className="app-container">
              <div className="main-content">
                <FriendList />
                <div className="message-section">
                  <MessageBox />
                  <SendMessage />
                </div>
              </div>
            </div>
          }
        />
      </Routes>
    </Router>
  );
}

export default App;
