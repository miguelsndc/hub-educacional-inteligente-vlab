import { useMutation, useQueryClient } from "@tanstack/react-query";
import {
    createResource,
    deleteResource,
    updateResource,
    type ResourcePayload,
} from "../services/resource";

export const useCreateResource = () => {
    const queryClient = useQueryClient();
    return useMutation({
        mutationFn: (payload: ResourcePayload) => createResource(payload),
        onSuccess: () => queryClient.invalidateQueries({ queryKey: ["resources"] }),
    });
};

export const useUpdateResource = (id: number) => {
    const queryClient = useQueryClient();
    return useMutation({
        mutationFn: (payload: ResourcePayload) => updateResource(id, payload),
        onSuccess: () => queryClient.invalidateQueries({ queryKey: ["resources"] }),
    });
};

export const useDeleteResource = () => {
    const queryClient = useQueryClient();
    return useMutation({
        mutationFn: (id: number) => deleteResource(id),
        onSuccess: () => queryClient.invalidateQueries({ queryKey: ["resources"] }),
    });
};