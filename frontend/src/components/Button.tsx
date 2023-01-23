import React from 'react';

interface Props {
    handleClick: () => void;
    text: string;
    className?: string;
}

const Button: React.FC<Props> = ({ handleClick, text, className }) => {
  return (
    <button className="bg-blue-600 hover:bg-blue-700 rounded-xl p-2 m-2" onClick={handleClick}>{text}</button>
  );
};

export default Button;