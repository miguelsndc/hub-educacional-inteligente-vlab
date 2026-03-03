import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Pagination } from "../components/Pagination";
import { ResourceTable } from "../components/ResourceTable";
import { useResources } from "../hooks/useResources";

export function ListPage() {
    const navigate = useNavigate();
    const [page, setPage] = useState(1);
    const { data, isLoading, isError } = useResources(page);

    return (
        <div className="max-w-5xl mx-auto px-4 py-8">
            <div className="flex items-center justify-between mb-6">
                <h1 className="text-xl font-semibold text-gray-800">
                    📚 Recursos Educacionais
                </h1>
                <button
                    onClick={() => navigate("/new")}
                    className="px-4 py-2 bg-indigo-600 text-white text-sm rounded-md hover:bg-indigo-700"
                >
                    + Novo recurso
                </button>
            </div>

            {isLoading && (
                <p className="text-gray-400 text-center py-12">Carregando...</p>
            )}
            {isError && (
                <p className="text-red-500 text-center py-12">
                    Erro ao carregar recursos.
                </p>
            )}
            {data && (
                <>
                    <ResourceTable resources={data.items} />
                    <Pagination page={data.page} pages={data.pages} onChange={setPage} />
                </>
            )}
        </div>
    );
}