import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { useDeleteResource } from "../hooks/useMutateResource";
import type { Resource } from "../services/resource";
import { ConfirmModal } from "./ConfirmModal";

interface Props {
    resources: Resource[];
}

export function ResourceTable({ resources }: Props) {
    const navigate = useNavigate();
    const deleteMutation = useDeleteResource();
    const [waitingDelete, setWaitingDelete] = useState<number | null>(null);

    function handleConfirmDelete() {
        if (waitingDelete !== null) {
            deleteMutation.mutate(waitingDelete);
            setWaitingDelete(null);
        }
    }

    if (resources.length === 0) {
        return (
            <p className="text-center text-gray-400 py-12">
                Nenhum recurso cadastrado ainda.
            </p>
        );
    }

    return (
        <>
            <table className="w-full text-sm">
                <thead>
                    <tr className="border-b text-left text-gray-500">
                        <th className="py-3 pr-4 font-medium">Título</th>
                        <th className="py-3 pr-4 font-medium">Tipo</th>
                        <th className="py-3 pr-4 font-medium">Tags</th>
                        <th className="py-3" />
                    </tr>
                </thead>
                <tbody>
                    {resources.map((resource) => (
                        <tr key={resource.id} className="border-b hover:bg-gray-50">
                            <td className="py-3 pr-4 font-medium">
                                <Link to={`/resource/${resource.id}`} className="hover:underline">
                                    {resource.title}
                                </Link>
                            </td>
                            <td className="py-3 pr-4 capitalize text-gray-600">
                                {resource.type}
                            </td>
                            <td className="py-3 pr-4">
                                <div className="flex flex-wrap gap-1">
                                    {resource.tags.map((tag) => (
                                        <span
                                            key={tag}
                                            className="bg-indigo-50 text-indigo-600 text-xs px-2 py-0.5 rounded-full"
                                        >
                                            {tag}
                                        </span>
                                    ))}
                                </div>
                            </td>
                            <td className="py-3 text-right whitespace-nowrap">
                                <button
                                    onClick={() => navigate(`/resource/edit/${resource.id}`)}
                                    className="text-indigo-600 hover:underline mr-4 text-sm"
                                >
                                    Editar
                                </button>
                                <button
                                    onClick={() => setWaitingDelete(resource.id)}
                                    className="text-red-500 hover:underline text-sm"
                                >
                                    Excluir
                                </button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>

            {waitingDelete !== null && (
                <ConfirmModal
                    message="Tem certeza que deseja excluir este recurso?"
                    onConfirm={handleConfirmDelete}
                    onCancel={() => setWaitingDelete(null)}
                />
            )}
        </>
    );
}