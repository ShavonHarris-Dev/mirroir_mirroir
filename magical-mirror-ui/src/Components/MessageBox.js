import React from 'react';

function MessageBox() {
  const messages = ['You are amazing!', 'Keep pushing forward!']; // From API

  return (
    <div className="message-box">
      <h3>Magical Mirror Messages</h3>
      <div className="mirror">
        {messages.map((message, index) => (
          <p key={index}>{message}</p>
        ))}
      </div>
    </div>
  );
}

export default MessageBox;
