import React, { useState } from 'react';

function SendMessage() {
  const [message, setMessage] = useState('');

  const handleSend = () => {
    // Handle send message logic
  };

  return (
    <div className="send-message">
      <textarea
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Enter your message..."
      />
      <button onClick={handleSend}>Send Message</button>
    </div>
  );
}

export default SendMessage;
