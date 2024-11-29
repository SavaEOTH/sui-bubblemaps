import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [walletAddress, setWalletAddress] = useState('');
  const [contractAddress, setContractAddress] = useState('');
  const [graphData, setGraphData] = useState(null);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');

    try {
      const response = await axios.post('/api/fetch_transactions', {
        wallet_address: walletAddress,
        contract_address: contractAddress
      });

      setGraphData(response.data);
    } catch (err) {
      setError('Failed to fetch transactions');
      console.error(err);
    }
  };

  return (
    <div style={{ maxWidth: '600px', margin: 'auto', padding: '20px' }}>
      <h1>Sui Transaction Visualizer</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>
            Wallet Address:
            <input 
              type="text" 
              value={walletAddress}
              onChange={(e) => setWalletAddress(e.target.value)}
              required
            />
          </label>
        </div>
        <div>
          <label>
            Contract Address:
            <input 
              type="text" 
              value={contractAddress}
              onChange={(e) => setContractAddress(e.target.value)}
              required
            />
          </label>
        </div>
        <button type="submit">Fetch Transactions</button>
      </form>

      {error && <p style={{ color: 'red' }}>{error}</p>}

      {graphData && (
        <div>
          <h2>Transaction Network</h2>
          <pre>{JSON.stringify(graphData, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
