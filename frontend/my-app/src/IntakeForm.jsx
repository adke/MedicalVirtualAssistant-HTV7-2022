import React, { useState } from "react";
import "./App.css";
import { MessageList } from "./MessageList";

const DUMMY_DATA = [
  {
    senderId: "Ayush",
    text: "who will win the Hackathon?",
  },
  {
    senderId: "Adish",
    text: "We might!",
  },
];

export const IntakeForm = () => {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [userConcern, setuserConcern] = useState("");
  const [messages, setMessage] = useState(DUMMY_DATA);
  const [showMessages, setShowMessages] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!name || !email || !userConcern) {
      setShowMessages(false);
    } else {
      setShowMessages(true);
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
          <button type="submit" className="btn btn-primary">
            Start Chat
          </button>
        </div>
      </form>
      {showMessages ? <MessageList messages={messages} /> : null}
    </div>
  );
};
