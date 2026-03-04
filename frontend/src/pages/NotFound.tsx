import { useNavigate } from "react-router-dom";

export function NotFoundPage() {
    const navigate = useNavigate();

    return (
        <div className="flex flex-col items-center justify-center min-h-screen text-center px-4">
            <p className="text-6xl font-bold text-indigo-600 mb-4">404</p>
            <h1 className="text-xl font-semibold text-gray-800 mb-2">
                Página não encontrada
            </h1>
            <p className="text-gray-500 mb-6">
                A página que você está procurando não existe.
            </p>
            <button
                onClick={() => navigate("/")}
                className="px-4 py-2 bg-indigo-600 text-white text-sm rounded-md hover:bg-indigo-700"
            >
                Voltar para a listagem
            </button>
        </div>
    );
}