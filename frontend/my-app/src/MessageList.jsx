export const MessageList = ({ messages }) => {
  return (
    <ul className="message-list">
      {messages.map((message) => {
        return (
          <li key={message.id}>
            <div>{message.senderId}</div>
            {message.text}
          </li>
        );
      })}
    </ul>
  );
};
