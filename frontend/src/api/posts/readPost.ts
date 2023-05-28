import axios from "@api/axiosInstance";
import { useQuery } from "@tanstack/react-query";
import { IPostDetail } from "@type/posts";

export const readPost = async (id: string) => {
  try {
    const response = await axios.get(`/posts/${id}`);
    return response.data;
  } catch (err) {
    console.log("🚀 readPost.tsx", err);
    return { data: [] };
  }
};

export const useReadPost = (id: string) => {
  return useQuery<IPostDetail>({
    queryKey: ["postDetail", id],
    queryFn: () => readPost(id),
    refetchOnMount: "always", // 유저폼 활성화를 위해 설정
  });
};
