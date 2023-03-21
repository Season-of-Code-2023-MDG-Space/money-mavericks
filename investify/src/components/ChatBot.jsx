import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../styles/ChatBot.css'

const ChatBot = () => {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');

  useEffect(() => {
    // Fetch initial messages from server
    axios.get('/api/messages')
      .then(response => {
        setMessages(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  const handleInputChange = event => {
    setInputValue(event.target.value);
  };

  const handleFormSubmit = event => {
    event.preventDefault();

    // Add new message to state and send to server
    const newMessage = { text: inputValue };
    setMessages([...messages, newMessage]);

    axios.post('/api/messages', newMessage)
      .then(response => {
        console.log(response);
      })
      .catch(error => {
        console.log(error);
      });

    // Clear input field
    setInputValue('');
  };

  return (
    <div className="chat-gpt">
      <div className="chat-gpt__messages">
        {messages.map((message, index) => (
          <div key={index} className="chat-gpt__message">
            <p>{message.text}</p>
          </div>
        ))}
      </div>
      <form onSubmit={handleFormSubmit}>
        <input type="text" value={inputValue} onChange={handleInputChange} />
        <button type="submit">Send</button>
      </form>
    </div>
  );
};

export default ChatBot;
