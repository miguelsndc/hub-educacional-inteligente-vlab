import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { FormPage } from "./pages/Form";
import { ListPage } from "./pages/List";
import { ResourcePage } from "./pages/Resource";

const queryClient = new QueryClient();

export default function App() {
    return (
        <QueryClientProvider client={queryClient}>
            <BrowserRouter>
                <Routes>
                    <Route path="/" element={<ListPage />} />
                    <Route path="/resource/new" element={<FormPage />} />
                    <Route path="/resource/:id" element={< ResourcePage />} />
                    <Route path="/resource/edit/:id" element={<FormPage />} />
                </Routes>
            </BrowserRouter>
        </QueryClientProvider>
    );
}