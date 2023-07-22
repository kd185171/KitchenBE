const express = require('express');
const bodyParser = require('body-parser');
const { exec } = require('child_process');
const pythonExecutable = 'C:\Users\kd185171\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.11';
 
const app = express();
const port = 3000;
 
app.use(bodyParser.json());

app.get('/getHourData', (req, res) => {
  exec(`python hour_data.py`, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error executing the Python script: ${error.message}`);
      return res.status(500).json({ error: 'Internal server error' });
    }
    let hourData;
    try {
      hourData = stdout.trim();
    } catch (e) {
      console.error('Error parsing Python script output:', e);
      return res.status(500).json({ error: 'Internal server error' });
    }
    return res.json(hourData);
  });
});

app.get('/getDayData', (req, res) => {
  exec(`python day_data.py`, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error executing the Python script: ${error.message}`);
      return res.status(500).json({ error: 'Internal server error' });
    }
    let dayData;
    try {
      dayData = stdout.trim();
    } catch (e) {
      console.error('Error parsing Python script output:', e);
      return res.status(500).json({ error: 'Internal server error' });
    }
    return res.json(dayData);
  });
}); 

 
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});