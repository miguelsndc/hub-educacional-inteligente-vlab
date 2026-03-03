import api from "./api"

export interface Resource {
    id: number;
    title: string;
    description: string | null;
    type: string;
    url: string | null;
    tags: string[];
    created_at: string;
    updated_at: string;
}

export interface PaginatedResponse {
    items: Resource[];
    total: number;
    page: number;
    limit: number;
    pages: number;
}

export interface ResourcePayload {
    title: string;
    description?: string;
    type: string;
    url?: string;
    tags: string[];
}

export const getResources = async (page: number, limit: number) => {
    const { data } = await api.get<PaginatedResponse>('/resources', { params: { page, limit } });
    return data;
}

export const getResource = async (id: number) => {
    const { data } = await api.get<Resource>(`/resources/${id}`);
    return data;
}

export const createResource = async (payload: ResourcePayload) => {
    const { data } = await api.post<Resource>('/resources', payload);
    return data;
}

export const updateResource = async (id: number, payload: ResourcePayload) => {
    const { data } = await api.put<Resource>(`/resources/${id}`, payload);
    return data;
}

export const deleteResource = async (id: number) => {
    await api.delete(`/resources/${id}`);
}

