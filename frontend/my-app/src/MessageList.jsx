export const MessageList = ({ messages }) => {
  return (
    <div>
      <ul className="message-list">
        {messages.map((message) => {
          return (
            <div>
              <li key={message.id}>
                <div className="sender-id">{message.senderId}</div>
                {message.text}
              </li>
            </div>
          );
        })}
      </ul>
    </div>
  );
};
