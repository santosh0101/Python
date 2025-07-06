import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [options, setOptions] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    axios.get('http://localhost:5001/cryptokeys')
      .then(res => setOptions(res.data))
      .catch(err => setError('Failed to load technologies'));
  }, []);

  return (
    <div style={{ padding: '2rem' }}>
      <h3>Select Residing Technology</h3>
      <select>
        {options.map((opt, idx) => <option key={idx}>{opt}</option>)}
      </select>
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
}

export default App;
