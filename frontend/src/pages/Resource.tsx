import { useQuery } from "@tanstack/react-query";
import { useLocation, useNavigate, useParams } from "react-router-dom";
import { getResource } from "../services/resource";
import { Chip } from "../components/Chip";

export function ResourcePage() {
    const { id } = useParams();
    const navigate = useNavigate();
    const location = useLocation();
    const isEditing = !!id;

    const { data, isLoading } = useQuery({
        queryKey: ["resource", id],
        queryFn: () => getResource(Number(id)),
        enabled: isEditing,
    });

    if (isEditing && isLoading) {
        return <p className="text-center text-gray-400 py-12">Carregando...</p>;
    }

    if (isEditing && !data) {
        return <p className="text-center text-red-500 py-12">Recurso não encontrado.</p>;
    }

    const formattedCreationDate = data?.created_at ? new Date(data.created_at).toLocaleDateString('pt-BR') : null;
    const formattedUpdateDate = data?.updated_at ? new Date(data.updated_at).toLocaleDateString('pt-BR') : null;

    return (
        <div className="max-w-2xl mx-auto px-4 py-8">
            <h1 className="text-4xl font-bold text-gray-800">{data?.title}</h1>
            <div className="flex items-center my-4">
                <span className="text-sm text-gray-500">Criado em: {formattedCreationDate}</span>
                {formattedUpdateDate && (
                    <>
                        <span className="text-sm text-gray-400 mx-2">|</span>
                        <span className="text-sm text-gray-500 block">Atualizado por último em: {formattedUpdateDate}</span>
                    </>
                )}
            </div>
            <div className="flex gap-2 mt-4">
                {data?.tags.map((tag) => {
                    return <Chip key={tag} tag={tag} />;
                })}
            </div>
            <p className="text-gray-600 mt-4">{data?.description}</p>
            <div className="flex items-center gap-x-4">
                {data?.url && (
                    <a
                        href={data.url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="mt-4 inline-block text-indigo-700 hover:text-indigo-500 underline rounded-md"
                    >
                        Acessar recurso
                    </a>
                )}
                <button
                    className="mt-4 bg-indigo-600 text-white px-4 py-2 rounded-md hover:bg-indigo-700 transition-colors"
                    onClick={() => navigate(`/resource/edit/${id}`, {
                        state: { from: location.pathname },
                    })}
                >
                    Editar recurso
                </button>
            </div>
        </div>
    );
}