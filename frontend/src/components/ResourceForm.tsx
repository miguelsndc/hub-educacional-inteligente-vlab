import { useState, type SubmitEvent } from "react";
import { useNavigate } from "react-router-dom";
import { useCreateResource, useUpdateResource } from "../hooks/useMutateResource";
import type { Resource, ResourcePayload } from "../services/resource";
import { TagInput } from "./TagInput";
import { FormField, Input, Select, Textarea } from "./Input";
import { useAISuggest } from "../hooks/useAISuggest";
import { Warning } from "./Warning";

const RESOURCE_TYPES = ["video", "pdf", "link"];

interface Props {
    initial?: Resource;
    onSuccess?: () => void;
}

export function ResourceForm({ initial, onSuccess }: Props) {
    const navigate = useNavigate();
    const createMutation = useCreateResource();
    const updateMutation = useUpdateResource(initial?.id ?? 0);

    const [title, setTitle] = useState(initial?.title ?? "");
    const [description, setDescription] = useState(initial?.description ?? "");
    const [type, setType] = useState(initial?.type ?? "");
    const [url, setUrl] = useState(initial?.url ?? "");
    const [tags, setTags] = useState<string[]>(initial?.tags ?? []);
    const [error, setError] = useState<string | null>(null);

    function handleTagChange(newTags: string[]) {
        setTags(newTags);
    };

    const { handleSuggest, loading: aiLoading, error: aiError } = useAISuggest({
        onSuccess: (desc, tags) => {
            setDescription(desc);
            setTags(tags);
        }
    })

    const editing = !!initial;
    const canSuggest = title.trim() !== "" && type !== "";
    const pending = createMutation.isPending || updateMutation.isPending;

    async function handleSubmit(e: SubmitEvent) {
        e.preventDefault();
        if (!title.trim()) {
            setError("O título é obrigatório.");
            return;
        }
        if (!type) {
            setError("O tipo é obrigatório.");
            return;
        }

        setError(null);
        const payload: ResourcePayload = { title, description, type, url, tags };

        try {
            if (editing) {
                await updateMutation.mutateAsync(payload);
            } else {
                await createMutation.mutateAsync(payload);
            }
            onSuccess?.();
        } catch (err: unknown) {
            if (err instanceof Error) {
                setError(err.message);
            } else {
                setError("Erro inesperado. Tente novamente.");
            }
        }
    };

    return (
        <form className="mx-auto flex flex-col gap-2" onSubmit={handleSubmit}>
            <h1 className="text-5xl font-medium">{editing ? "Editar Recurso" : "Criar novo Recurso"}</h1>
            <p className="text-sm text-gray-500">Preencha os campos abaixo:</p>
            <FormField label="Título" for="title" required>
                <Input name="title" value={title} onChange={(e) => setTitle(e.target.value)} required />
            </FormField>

            <TagInput tags={tags} onChange={handleTagChange} />

            <FormField label="Tipo" for="type" required>
                <Select
                    name="type"
                    value={type}
                    required
                    onChange={(e) => setType(e.target.value)}
                >
                    <option value="">Selecione...</option>
                    {RESOURCE_TYPES.map((t) => (
                        <option key={t} value={t}>
                            {t.charAt(0).toUpperCase() + t.slice(1)}
                        </option>
                    ))}
                </Select>
            </FormField>

            <button
                type="button"
                onClick={() => handleSuggest(title, type)}
                disabled={!canSuggest || aiLoading}
                className="w-full py-2 rounded-md bg-violet-600 text-white text-sm font-medium hover:bg-violet-700 disabled:opacity-40 transition"
            >
                {aiLoading
                    ? "Consultando assistente pedagógico..."
                    : "Gerar Descrição com IA"}
            </button>

            {aiError && <Warning text={aiError} />}

            <FormField label="Descrição" for="description">
                <Textarea
                    name="description"
                    value={description ?? ""}
                    onChange={(e) => setDescription(e.target.value)}
                    rows={4}
                    className="w-full border rounded-md px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500"
                />
            </FormField>

            <FormField label="Url" for="url">
                <Input type="url" name="url" value={url ?? ""} onChange={(e) => setUrl(e.target.value)} placeholder="https://exemplo.com" />
            </FormField>


            {error && (
                <p className="text-sm text-red-600 bg-red-50 border border-red-200 rounded-md px-3 py-2">
                    {error}
                </p>
            )}

            <div className="flex justify-end gap-3 pt-2">
                <button
                    type="button"
                    onClick={() => navigate("/")}
                    className="px-4 py-2 rounded border text-sm text-gray-600 hover:bg-gray-50"
                >
                    Cancelar
                </button>
                <button
                    type="submit"
                    disabled={pending}
                    className="px-4 py-2 rounded bg-indigo-600 text-white text-sm hover:bg-indigo-700 disabled:opacity-40"
                >
                    {editing ? "Salvar alterações" : "Criar recurso"}
                </button>
            </div>
        </form>
    );
};