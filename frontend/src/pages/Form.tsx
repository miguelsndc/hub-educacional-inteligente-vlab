import { useQuery } from "@tanstack/react-query";
import { useParams } from "react-router-dom";
import { ResourceForm } from "../components/ResourceForm";
import { getResource } from "../services/resource";

export function FormPage() {
    const { id } = useParams();
    const isEditing = !!id;

    const { data, isLoading } = useQuery({
        queryKey: ["resource", id],
        queryFn: () => getResource(Number(id)),
        enabled: isEditing,
    });

    if (isEditing && isLoading) {
        return <p className="text-center text-gray-400 py-12">Carregando...</p>;
    }

    return (
        <div className="max-w-2xl mx-auto px-4 py-8">
            <ResourceForm initial={isEditing ? data : undefined} />
        </div>
    );
}