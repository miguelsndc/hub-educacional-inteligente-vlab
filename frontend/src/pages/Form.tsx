import { useQuery } from "@tanstack/react-query";
import { useNavigate, useParams } from "react-router-dom";
import { ResourceForm } from "../components/ResourceForm";
import { getResource } from "../services/resource";
import { useEffect } from "react";

export function FormPage() {
    const { id } = useParams();
    const navigate = useNavigate();

    const isEditing = !!id;

    const { data, isLoading, isError } = useQuery({
        queryKey: ["resource", id],
        queryFn: () => getResource(Number(id)),
        enabled: isEditing,
        retry: false,
    });

    useEffect(() => {
        if (isError) {
            navigate("/not-found");
        }
    }, [isError, navigate]);

    function handleFormSuccess(id: number) {
        navigate(`/${id}`);
    }

    if (isEditing && isLoading) {
        return <p className="text-center text-gray-400 py-12">Carregando...</p>;
    }

    return (
        <div className="max-w-2xl mx-auto px-4 py-8">
            <ResourceForm initial={isEditing ? data : undefined} onSuccess={handleFormSuccess} />
        </div>
    );
}