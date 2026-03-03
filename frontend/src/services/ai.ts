import api from "./api"

export interface AIRequest {
    title: string;
    type: string;
}

export interface AIResponse {
    description: string;
    tags: string[];
}

export const suggest = async (payload: AIRequest) => {
    const { data } = await api.post<AIResponse>('/ai/suggest', payload);
    return data;
}
