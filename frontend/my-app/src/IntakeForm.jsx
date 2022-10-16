import React, { useState } from "react";
import "./App.css";
import { MessageList } from "./MessageList";
import axios from 'axios';

const DUMMY_DATA = [
  {
    senderId: "Health Assistant",
    text: "No input provided",
  },
];

export const IntakeForm = () => {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [userConcern, setuserConcern] = useState("");
  const [messages, setMessage] = useState(DUMMY_DATA);
  const [showMessages, setShowMessages] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!name || !email || !userConcern) {
      return;
    } else {
      console.log(name)
      const res = await axios({
        method: 'POST',
        url: 'http://127.0.0.1:8000/predict',
        headers: {
          "accept": "application/json",
          "Content-Type": "application/json",
        },
        data: {
          'symptoms': [userConcern]
        }
      })
      console.log(res)
      setShowMessages(true);

      let output_text = "Based on your symptoms, you could have one of the following: " + res.data.class
      setMessage([{
        senderId: "Health Assistant:",
        text: output_text
      }])
    }
  };

  return (
    <div>
      <form className="intake-form" onSubmit={handleSubmit}>
        <p className="text">
          Please fill out the following information to make use of the of the
          Health Bot
        </p>
        <input
          type="text"
          placeholder="Enter your name"
          name="name"
          required
          onChange={(e) => setName(e.target.value)}
        />

        <input
          type="email"
          placeholder="Enter your email"
          name="email"
          required
          onChange={(e) => setEmail(e.target.value)}
        />

        <input
          type="text"
          placeholder="Please enter if you have any concerns or any symptoms you are experiencing"
          name="userConcern"
          required
          onChange={(e) => setuserConcern(e.target.value)}
        />

        <div className="submit-button">
          <button
            id="start-chat-button"
            type="submit"
            className="btn btn-primary"
          >
            Start Chat
          </button>
        </div>
      </form>
      {showMessages ? <MessageList messages={messages} /> : null}
    </div>
  );
};
