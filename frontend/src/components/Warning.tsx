interface Props {
    text: string;
}
export function Warning({ text }: Props) {
    return <p className="text-sm text-yellow-700 bg-yellow-50 border border-yellow-200 rounded-md px-3 py-2">
        {text}
    </p>
}