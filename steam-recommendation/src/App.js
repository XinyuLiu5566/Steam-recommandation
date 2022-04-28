import './App.css';
import React, { useState } from 'react';
import Table from 'react-bootstrap/Table'
import Button from 'react-bootstrap/Button'
import Form from 'react-bootstrap/Form'


function App() {
  const [games, setGames] = useState([])
  const [playTimes, setPlayTimes] = useState([])
  const [name, setName] = useState('')
  const [time, setTime] = useState('')
  const [recommended, setRecommended] = useState([])
  const [visible, setVisible] = useState(false)

  const handleGame = (e) => {
    const {value} = e.target
    setName(value)
  }

  const handleTime = (e) => {
    const {value} = e.target
    setTime(value)
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    setGames([...games, name])
    setPlayTimes([...playTimes, time])
    setName('')
    setTime('')
  }
  const data = {
    games: games,
    playTimes: playTimes
  }

  const getRecommendedGames = (e) => {
    e.preventDefault()
    alert('The table will show after the execution')
    fetch('http://127.0.0.1:5000/get_game', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(res => 
      setRecommended(res.recommend),
      setVisible(true),
    )
}


  return (
    <div>
      <Form className='form-inline' onSubmit={handleSubmit}>
        <Form.Group className="mb-3" controlId="formBasicEmail">
          <Form.Label>Game</Form.Label>
          <Form.Control type="text" name="game" value={name} onChange={handleGame}/>
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBasicPassword">
          <Form.Label>Play Time</Form.Label>
          <Form.Control type="text" name="playtime" value={time} onChange={handleTime} />
        </Form.Group>
        <Button variant="primary" type="submit" value="Submit">
          SUBMIT
        </Button>
      </Form>
      <br></br>
      <div className='table1'>
        <h4>Favorite games</h4>
        <Table bordered hover>
          <thead>
            <tr>
              <th>#</th>
              <th>Game</th>
              <th>Playtime</th>
            </tr>
          </thead>
          <tbody>
          {
            games.map((item, index) => {
              return (
                <tr key={item}>
                  <td>{index+1}</td>
                  <td>{games[index]}</td>
                  <td>{playTimes[index]}</td>
                </tr>
              )
            })
          }
        </tbody>
      </Table>
    </div>
    <div className='table2'>
    {visible?
    <div>
      <h4>Recommended games</h4>
      <Table  striped bordered hover>
        <thead>
          <tr>
            <th>#</th>
            <th>Game</th>
          </tr>
        </thead>
        <tbody>
        {
          recommended.map((item, index) => {
            return (
              <tr key={item}>
                <td>{index+1}</td>
                <td>{recommended[index]}</td>
              </tr>
            )
          })
        }
      </tbody>
    </Table>
    </div>
    : 
    <Button variant="primary" onClick={getRecommendedGames}>
    Get Recommended Games
    </Button>}
      
    </div>
  </div>
  );
}

export default App;






