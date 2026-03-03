/// <reference types="vite/types/importMeta.d.ts" />

import axios from 'axios';

const api = axios.create({
    baseURL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000',
});

api.interceptors.response.use(
    (res) => res,
    (error) => {
        const message = error.response?.data?.detail ?? "Erro inesperado. Por favor, tente novamente.";
        return Promise.reject(new Error(message));
    }
)

export default api;