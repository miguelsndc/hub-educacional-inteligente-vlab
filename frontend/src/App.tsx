import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { FormPage } from "./pages/Form";
import { ListPage } from "./pages/List";
import { NotFoundPage } from "./pages/NotFound";
import { ResourcePage } from "./pages/Resource";

const queryClient = new QueryClient();

export default function App() {
    return (
        <QueryClientProvider client={queryClient}>
            <BrowserRouter>
                <Routes>
                    <Route path="/" element={<ListPage />} />
                    <Route path="/new" element={<FormPage />} />
                    <Route path="/:id" element={<ResourcePage />} />
                    <Route path="/edit/:id" element={<FormPage />} />
                    <Route path="/not-found" element={<NotFoundPage />} />
                    <Route path="*" element={<NotFoundPage />} />
                </Routes>
            </BrowserRouter>
        </QueryClientProvider>
    );
}