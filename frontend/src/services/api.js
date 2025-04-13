// src/services/api.js
import axios from 'axios';

const isBioed = window.location.hostname === 'bioed-new.bu.edu';

const api = axios.create({
  baseURL: isBioed
    ? '/students_25/Team10/PerturBase/main' // bioed server
    : '', // use locally
});

export default api;