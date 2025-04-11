import axios from 'axios';

const api = axios.create({
  baseURL: process.env.REACT_APP_API_URL || '/students_25/Team10/PerturBase/main/',
});

export default api;