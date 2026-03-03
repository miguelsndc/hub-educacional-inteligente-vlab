interface Props {
    tag: string;
    handleTagRemove?: (tag: string) => void;
}
export function Chip({ tag, handleTagRemove }: Props) {
    function handleRemove(tag: string) {
        handleTagRemove?.(tag);
    }
    return <span
        key={tag}
        className="inline-flex items-center gap-1 bg-indigo-100 text-indigo-700 text-sm px-2 py-1 rounded-full"
    >
        {tag}
        {handleTagRemove && (
            <button
                type="button"
                onClick={() => handleRemove(tag)}
                className="hover:text-red-500 leading-none cursor-pointer"
            >
                <span>×</span>
            </button>)
        }
    </span>
}