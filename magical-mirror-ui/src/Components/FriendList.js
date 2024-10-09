import React, { useState, useEffect } from 'react';
import axios from 'axios';

function FriendList() {
  const [friends, setFriends] = useState([]);

  useEffect(() => {
    axios.get('/api/friends')
      .then(response => setFriends(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div className="friend-list">
      <h3>Your Friends</h3>
      <ul>
        {friends.map((friend) => (
          <li key={friend.id}>{friend.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default FriendList;

