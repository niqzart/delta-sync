import { Tooltip, TooltipContent, TooltipTrigger } from "@/shared/ui/tooltip"
import { StrictMode } from "react"
import { createRoot } from "react-dom/client"
import "./index.css"

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <Tooltip>
      <TooltipTrigger asChild>
        <h1 className="scroll-m-20 text-center text-4xl font-extrabold tracking-tight text-balance">
          Delta Sync
        </h1>
      </TooltipTrigger>
      <TooltipContent>
        <p className="w-80">
          Delta-based synchronization demo web application made with FastAPI, SocketIO (TMEXIO), SQLAlchemy, React & Vite
        </p>
      </TooltipContent>
    </Tooltip>
  </StrictMode>,
)
