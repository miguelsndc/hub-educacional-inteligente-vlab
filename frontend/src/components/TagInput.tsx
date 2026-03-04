import { useState, type KeyboardEvent } from "react"
import { FormField, Input } from "./Input";
import { Warning } from "./Warning";
import { Chip } from "./Chip";

interface Props {
    tags: string[]
    onChange?: (tags: string[]) => void
}

export function TagInput({ tags, onChange }: Props) {
    const [input, setInput] = useState("")
    const [warning, setWarning] = useState<string | null>(null)

    function normalize(tag: string) {
        //                                    qualquer quantidade de espaço vazio é removida
        return tag.trim().toLowerCase().split(/\s+/).join("-");
    }

    function addTag() {
        setWarning(null);

        if (tags.length >= 10) {
            setWarning("Limite de 10 tags atingido.");
            return;
        }

        const normalized = normalize(input);

        if (normalized === "") return;

        if (normalized.length > 50) {
            setWarning("Uma tag pode ter no máximo 50 caracteres.");
            return;
        }

        if (tags.includes(normalized)) {
            setWarning("Esta tag já foi adicionada.");
            return;
        }

        onChange?.([...tags, normalized]);
        setInput("");
    }

    function handleKeyDown(e: KeyboardEvent<HTMLInputElement>) {
        if (e.key === "Enter" && input.trim() !== "") {
            e.preventDefault();
            addTag();
            setInput("");
            setWarning(null);
        }
    }

    function handleTagRemove(tagToRemove: string) {
        const newTags = tags.filter(tag => tag !== tagToRemove);
        onChange?.(newTags);
        setWarning(null);
    }

    return (
        <FormField label="Tags" for="tag-input">
            <div className="flex flex-wrap gap-2 mb-3">
                {tags.map((tag) => (
                    <Chip key={tag} tag={tag} handleTagRemove={handleTagRemove} />
                ))}
            </div>

            <Input
                id="tag-input"
                name="tag-input"
                value={input}
                placeholder="Adicionar tag..."
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={handleKeyDown}
            />

            {warning && <Warning text={warning} />}
        </FormField>
    )
}