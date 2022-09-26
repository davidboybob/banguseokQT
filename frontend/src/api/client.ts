import axios from "axios";

let urls = {
    test: "http://localhost:5000/api/v1",
    development: "http://localhost:5000/api/v1",
    production: "http://localhost:5000/api/v1",
}


export const client = axios.create({
    // baseURL: urls['development'],
    baseURL: "/api/v1",
    headers: {
        Accept: "application/json",
        "Content-type": "application/json",
    },
});