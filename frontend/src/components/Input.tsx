const baseStyles =
    `w-full rounded-md border border-gray-300 placeholder-gray-600
     px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500`;

export function Input(props: React.InputHTMLAttributes<HTMLInputElement>) {
    return <input {...props} className={baseStyles + (props.className ?? " ")} />;
}

export function Select(props: React.SelectHTMLAttributes<HTMLSelectElement>) {
    return <select {...props} className={baseStyles + (props.className ?? " ")} />;
}

export function Textarea(props: React.TextareaHTMLAttributes<HTMLTextAreaElement>) {
    return <textarea {...props} className={baseStyles + (props.className ?? " ")} />;
}

interface FormFieldProps {
    label: string;
    for: string;
    required?: boolean;
    children: React.ReactNode;
}

/**
 * No momento é necessário passar o for e o name pro input com o mesmo valor, uma opção
 * é usar um context por field e gerar o id nele com useId, e cada campo de input consome esse id, porém pro
 * escopo do projeto é overengineering, então por ora deixei dessa forma mesmo, mas é algo a se considerar no futuro
 */

export function FormField({ label, for: htmlFor, required, children }: FormFieldProps) {
    return (
        <div className="mb-4 flex flex-col gap-2">
            <div className="flex items-center gap-x-1">
                <label htmlFor={htmlFor} className="block font-medium text-gray-700 mb-1">{label}</label>
                {required && <span className="text-sm text-red-600">*</span>}
            </div>
            {children}
        </div>
    );
}