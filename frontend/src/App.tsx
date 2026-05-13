interface ButtonProps {
  text: string; 
}

const Button = ({ text }: ButtonProps) => (
  <button onClick={() => console.log("Hi")}>{text}</button>
)

export default function App() {
  return (
    <div>
      <Button text="Something" />
    </div>
  )
}