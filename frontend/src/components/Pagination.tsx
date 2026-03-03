interface Props {
    page: number;
    pages: number;
    onChange: (page: number) => void;
}

export function Pagination({ page, pages, onChange }: Props) {
    if (pages <= 1) return null;

    return (
        <div className="flex items-center gap-2 justify-center mt-6">
            <button
                onClick={() => onChange(page - 1)}
                disabled={page === 1}
                className="px-3 py-1 rounded border text-sm disabled:opacity-40 hover:bg-gray-50"
            >
                ←
            </button>
            <span className="text-sm text-gray-600">
                {page} de {pages}
            </span>
            <button
                onClick={() => onChange(page + 1)}
                disabled={page === pages}
                className="px-3 py-1 rounded border text-sm disabled:opacity-40 hover:bg-gray-50"
            >
                →
            </button>
        </div>
    );
}