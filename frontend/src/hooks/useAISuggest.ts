import { useState } from "react";
import { suggest } from "../services/ai";

interface Props {
    onSuccess: (description: string, tags: string[]) => void
}

export function useAISuggest({ onSuccess }: Props) {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);


    const handleSuggest = async (title: string, type: string) => {
        setLoading(true);
        setError(null);
        try {
            const res = await suggest({ title, type });
            onSuccess(res.description, res.tags);
        } catch (err: unknown) {
            if (err instanceof Error) {
                setError(err.message);
            } else {
                setError("Erro inesperado. Tente novamente.");
            }
        } finally {
            setLoading(false);
        }
    }

    return { handleSuggest, loading, error };
}