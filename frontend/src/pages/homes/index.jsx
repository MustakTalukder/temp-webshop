import Header1 from "@/components/headers/Header1";
import Home from "@/components/homes/Home";
import MetaComponent from "@/components/common/MetaComponent";
const metadata = {
  title: "Home",
  description: "Home Page",
};
export default function HomePage() {
  return (
    <>
      <MetaComponent meta={metadata} />
      <Header1 />
      <main className="page-wrapper">
        <div className="mb-4 pb-4"></div>
        <Home />
      </main>
    </>
  );
}
