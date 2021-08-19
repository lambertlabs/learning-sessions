export const App = () => {
  const initialCounter = 0;
  const [counter, setCounter] = React.useState(initialCounter);
  // const handleAdd = () => {
  //   setCounter(counter + 1);
  // };
  // const handleAdd = () => {
  //   setTimeout(() => setCounter(counter + 1), 5000);
  // };
  const handleAdd = () => {
    setTimeout(() => setCounter((prevCounter) => prevCounter + 1), 5000);
  };

  const handleReset = () => {
    setCounter(initialCounter);
  };
  const style = {
    padding: 16,
  };
  return (
    <>
      <div style={style}>Counter: {counter}</div>
      <div style={style}>
        <button onClick={handleAdd}>Add</button>
      </div>
      <div style={style}>
        <button onClick={handleReset}>Reset</button>
      </div>
    </>
  );
};
