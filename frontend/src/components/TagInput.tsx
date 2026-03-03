import { useState, type KeyboardEvent } from "react"
import { FormField, Input } from "./Input";
import { Warning } from "./Warning";

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
        const normalized = normalize(input);
        if (normalized === "") return;
        if (tags.includes(normalized)) {
            setWarning("Esta tag já foi adicionada.");
            return;
        }
        const newTags = [...tags, normalized];
        onChange?.(newTags);
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
                    <span
                        key={tag}
                        className="flex items-center gap-1 bg-indigo-100 text-indigo-700 text-sm px-2 py-1 rounded-full"
                    >
                        {tag}
                        <button
                            type="button"
                            onClick={() => handleTagRemove(tag)}
                            className="hover:text-red-500 leading-none cursor-pointer"
                        >
                            <span>×</span>
                        </button>
                    </span>
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