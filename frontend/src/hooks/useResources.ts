import { useQuery } from "@tanstack/react-query";
import { getResources } from "../services/resource";

export const useResources = (page: number, limit: number = 10) => {
    return useQuery({
        queryKey: ['resources', page, limit],
        queryFn: () => getResources(page, limit),
    })
}